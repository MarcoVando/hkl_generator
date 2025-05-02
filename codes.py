from https://github.com/cheminfo-py/xrd-tools/blob/master/xrd_tools/laue_predictor.py

wavelength = self.wavelength
latt = structure.lattice
is_hex = latt.is_hexagonal()

# Obtained from Bragg condition. Note that reciprocal lattice
# vector length is 1 / d_hkl.
min_r, max_r = (
    (0, 2 / wavelength)
    if two_theta_range is None
    else [2 * sin(radians(t / 2)) / wavelength for t in two_theta_range]
)

# Obtain crystallographic reciprocal lattice points within range
recip_latt = latt.reciprocal_lattice_crystallographic
recip_pts = recip_latt.get_points_in_sphere([[0, 0, 0]], [0, 0, 0], max_r)
if min_r:
    recip_pts = [pt for pt in recip_pts if pt[1] >= min_r]

peaks = {}
two_thetas = []

for hkl, g_hkl, ind, _ in sorted(
    recip_pts, key=lambda i: (i[1], -i[0][0], -i[0][1], -i[0][2])
):
    # Force miller indices to be integers.
    hkl = [int(round(i)) for i in hkl]
    if g_hkl != 0:

        d_hkl = 1 / g_hkl

        # Bragg condition
        theta = asin(wavelength * g_hkl / 2)

        two_theta = degrees(2 * theta)

        if is_hex:
            # Use Miller-Bravais indices for hexagonal lattices.
            hkl = (hkl[0], hkl[1], -hkl[0] - hkl[1], hkl[2])
        # Deal with floating point precision issues.
        ind = np.where(
            np.abs(np.subtract(two_thetas, two_theta))
            < AbstractDiffractionPatternCalculator.TWO_THETA_TOL
        )
        if len(ind[0]) > 0:
            peaks[two_thetas[ind[0][0]]][0] += 1.0
            peaks[two_thetas[ind[0][0]]][1].append(tuple(hkl))
        else:
            peaks[two_theta] = [1.0, [tuple(hkl)], d_hkl]
            two_thetas.append(two_theta)

x = []
y = []
hkls = []
d_hkls = []
for k in sorted(peaks.keys()):
    v = peaks[k]
    fam = get_unique_families(v[1])

    x.append(k)
    y.append(v[0])
    hkls.append(
        [{"hkl": hkl, "multiplicity": mult} for hkl, mult in fam.items()]
    )
    d_hkls.append(v[2])