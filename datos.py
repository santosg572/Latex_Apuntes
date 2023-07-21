t5 = '''
# Differential Geometry

Preface
Differential geometry studies properties of curves, surfaces, and smooth manifolds
by methods of mathematical analysis. Riemannian geometry is a section of differential
geometry which studies smooth manifolds with an additional structure,
Riemannian metric. The main part of this book is devoted to exactly Riemannian
geometry. The exception is affine differential geometry, projective differential
geometry, and connections more general than the Levi-Civitá connection, which
originates from a Riemannian metric.
The book begins with the simplest object of differential geometry, curves in the
plane. The most important characteristic of a curve at a given point is curvature.
The first chapter considers both local properties of curvature (the Frenet–Serret
formula and osculating circles) and global ones (the total curvature of a closed
curve and the four-vertex theorem). The total oriented curvature of a closed curve
is invariant with respect to a regular homotopy, and vice versa: if the total oriented
curvatures of two curves are equal, then these curves are regularly homotopic (this
is the Whitney–Graustein theorem). To each curve corresponds its evolute, that is,
the locus of centers of all osculating circles of this curve, that is, the envelope of the
family of normals.With respect to its evolute, the given curve is an involute. But the
inverse operation of assigning an involute to a curve is ambiguous: every curve has
a whole family of involutes (a curve orthogonal to a family of normals can be drawn
through every point of a normal).We give two proofs of the isoperimetric inequality
between the length of a closed curve without self-intersections and the area which
it bounds. A part of the differential geometry of plane curves is not related to a
Riemannian metric, that is, remains beyond the scope of Riemannian geometry. It
includes enveloping families of curves, affine unimodular differential geometry, and
projective differential geometry. The chapter about plane curves is concluded by
elements of integral geometry: we derive a formula expressing the measure of a set
of straight lines intersecting a given curve.
The second chapter studies curves in spaces, first in three-dimensional space
and then in many-dimensional ones. Given a curve in three-dimensional space, we
define curvature and torsion, derive the Frenet–Serret formula, and define osculating
planes and spheres. We also define the total curvature of a closed curve and prove
v


Fenchel’s theorem (that the total curvature of a closed curve is at least 2π) and
the Fáry-Milnor theorem (that the total curvature of a knotted closed curve is at
least 4π). At the end of the chapter, we consider curves in many-dimensional space,
define quantities generalizing curvature and torsion for such curves, and derive the
generalized Frenet–Serret formulas.
The third chapter is devoted to surfaces in three-dimensional space. On a surface
in R3, the first quadratic form is introduced; this is the inner product of tangent
vectors to the surface. With a curve on a surface, we associate a Darboux frame
and use it to define the geodesic curvature, the normal curvature, and the geodesic
torsion of a curve on a surface. A geodesic on a surface is a curve with zero geodesic
curvature; any shortest curve on a surface joining two given points is geodesic.
On a surface in R3, the second quadratic form is also defined. In a basis with
respect to which the matrix of the first quadratic form is the identity matrix and
the matrix of the second quadratic form is diagonal, the diagonal elements of the
second quadratic form are the principal curvatures. The Gaussian curvature of a
surface is the product of principal curvatures. The principal curvatures cannot be
expressed only in terms of the first quadratic form, but the Gaussian curvature can.
The Gaussian curvature of a surface can also be defined in a different way, in terms
of differential forms on the surface. The integral of the Gaussian curvature over
a polygon on the surface can be related to the integral of the geodesic curvature
over the boundary of this polygon and the sum of exterior angles of the polygon
(the Gauss–Bonnet formula). We define the parallel transport of a vector along a
curve and the covariant differentiation of vector fields and introduce the Riemannian
curvature tensor. Using geodesics, we define the exponentialmap of a tangent space
to a surface. To study properties of geodesics, we derive the first and the second
variation formula. Using Jacobi vector fields and conjugate points, we find out when
the length of a geodesic is not globally minimal.We prove the theorem on the local
isometry of surfaces of constant Gaussian curvature. At the end of the chapter, we
introduce the Laplace–Beltrami operator, which is a generalization to surfaces of
the Laplace operator in the plane.
In the fourth chapter we discuss two topics, hypersurfaces in many-dimensional
space and connections on vector bundles. The study of connections on vector
bundles is based on certain prerequisites concerning manifolds and vector bundles
over manifolds. Thus, beginning in Chap. 4, the reader is supposed to have
background knowledge of manifolds, tangent vectors, differential forms, vector
bundles over manifolds, sections of bundles, and the inverse function theorem;
all the necessary information can be found in the books [Pr2] and [Pr3]. For a
hypersurface in Euclidean space, we define the Weingarten operator and use it to
introduce the second, third, etc. quadratic forms. We define connections first on
hypersurfaces and then on any manifolds and vector bundles over manifolds. In
parallel, we introduce geodesics with respect to a given connection.We also define
the curvature tensor and the torsion tensor of a given connection and introduce the
curvature matrix of a connection.
The fifth chapter is concerned with the general theory of Riemannian manifolds.
A Riemannian manifold is a manifold whose every tangent space is equipped with

An inner product (Riemannian metric). On a Riemannian manifold, there exists a
unique torsion-free connection compatible with the Riemannian metric (the Levi-
Cività connection). The Riemann tensor of this connection has several symmetries
(satisfies several identities). Geodesics on Riemannianmanifolds have some specific
features in comparison with geodesics for arbitrary connections; in particular, any
such geodesic is locally a shortest curve. A Riemannian manifold is said to be
geodesically complete if all geodesics on this manifold can be extended without
bound. According to the Hopf–Rinowtheorem, geodesic completeness is equivalent
to the completeness of the Riemannian manifold as a metric space. The Riemann
tensor can be described by using the sectional curvatures corresponding to twodimensional
subspaces. For Riemannian submanifolds, as well as for hypersurfaces,
we can introduce the second quadratic form and prove generalizations of Gauss’
and Weingarten’s formulas. An important class of Riemannian submanifolds is
formed by totally geodesic submanifolds (a submanifold M is totally geodesic if
each geodesic on M is also a geodesic on the ambient manifold). In the manydimensional
case, just as in the case of surfaces, we obtain the first and the second
variation formulas and use them to introduce Jacobi fields and define conjugate
points. The chapter is concluded by a discussion of the holonomy (transformations
of the tangent space obtained by the parallel transport of vectors along closed
curves) and an interpretation of curvature as infinitesimal holonomy.
The sixth chapter discusses the differential geometry of Lie groups, that is,
manifolds endowed with a group structure consistent with the smooth structure.
With each Lie group, its Lie algebra is associated, which is the tangent space at
the identity element in which the multiplication of elements is defined as taking the
commutator of the left-invariant vector fields corresponding to tangent vectors. The
Lie algebra of a Lie group is mapped to this Lie group by the exponential map.
For a Lie group and a Lie algebra, adjoint representations are defined; the adjoint
representation of a Lie algebra is used to define the Killing form. On a Lie group,
there exist various connections and metrics related to the group structure in various
ways. On a compact Lie group, invariant integration can be defined. Some properties
of Lie groups are possessed by more general spaces, namely, by homogeneous and
symmetric ones.
The last (seventh) chapter is devoted to some of the applications of differential
geometry: comparison theorems, relationship between curvature and topological
properties of manifolds, and the Laplace operator on Riemannian manifolds.



1 Curves in the Plane 
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.1 Curvature and the Frenet–Serret Formulas 
. . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Osculating Circles 
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.3 The Total Curvature of a Closed Plane Curve
. . . . . . . . . . . . . . . . . . . . . . . . 7
1.4 Four-Vertex Theorem
.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.5 The Natural Equation of a Plane Curve
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
1.6 Whitney–Graustein Theorem
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
1.7 Tube Area and Steiner’s Formula
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
1.8 The Envelope of a Family of Curves
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
1.9 Evolute and Involute
.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
1.10 Isoperimetric Inequality
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
1.11 Affine Unimodular Differential Geometry
. . . . . . . . . . . . . . . . . . . . . . . . . . . 26
1.12 Projective Differential Geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
1.13 The Measure of the Set of Lines Intersecting a Given Curve.. . . . . . . 33
1.14 Solutions of Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
2 Curves in Space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
2.1 Curvature and Torsion: The Frenet–Serret Formulas . . . . . . . . . . . . . . . . 47
2.2 An Osculating Plane . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
2.3 Total Curvature of a Closed Curve .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
2.4 Bertrand Curves. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
2.5 The Frenet–Serret Formulas in Many-Dimensional Space . . . . . . . . . . 56
2.6 Solutions of Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
3 Surfaces in Space. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
3.1 The First Quadratic Form . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
3.2 The Darboux Frame of a Curve on a Surface . . . . . . . . . . . . . . . . . . . . . . . . 68
3.3 Geodesics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
3.4 The Second Quadratic Form . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
3.5 Gaussian Curvature .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
3.6 Gaussian Curvature and Differential Forms . . . . . . . . . . . . . . . . . . . . . . . . . . 77
3.7 The Gauss–Bonnet Theorem .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
ix

3.8 Christoffel Symbols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
3.9 The Spherical Gauss Map . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
3.10 The Geodesic Equation .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
3.11 Parallel Transport Along a Curve . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
3.12 Covariant Differentiation .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
3.13 The Gauss and Codazzi–Mainardi Equations . . . . . . . . . . . . . . . . . . . . . . . . 97
3.14 Riemann Curvature Tensor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
3.15 ExponentialMap. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
3.16 Lines of Curvature and Asymptotic Lines . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
3.17 Minimal Surfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
3.18 The First Variation Formula .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
3.19 The Second Variation Formula .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
3.20 Jacobi Vector Fields and Conjugate Points . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
3.21 Jacobi’s Theorem on a Normal Spherical Image .. . . . . . . . . . . . . . . . . . . . 122
3.22 Surfaces of Constant Gaussian Curvature . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
3.23 Rigidity (Unbendability) of the Sphere . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
3.24 Convex Surfaces: Hadamard’s Theorem.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
3.25 The Laplace–Beltrami Operator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
3.26 Solutions of Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
4 Hypersurfaces in Rn+1: Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
4.1 The Weingarten Operator.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
4.2 Connections on Hypersurfaces .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148
4.3 Geodesics on Hypersurfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
4.4 Convex Hypersurfaces .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
4.5 Minimal Hypersurfaces.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
4.6 Steiner’s Formula . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152
4.7 Connections on Vector Bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 153
4.8 Geodesics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156
4.9 The Curvature Tensor and the Torsion Tensor . . . . . . . . . . . . . . . . . . . . . . . 159
4.10 The Curvature Matrix of a Connection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
4.11 Solutions of Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167
5 Riemannian Manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
5.1 Levi-Cività Connection.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
5.2 Symmetries of the Riemann Tensor. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
5.3 Geodesics on Riemannian Manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173
5.4 The Hopf–Rinow Theorem.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
5.5 The Existence of Complete Riemannian Metrics . . . . . . . . . . . . . . . . . . . . 178
5.6 Covariant Differentiation of Tensors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
5.7 Sectional Curvature .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
5.8 Ricci Tensor .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
5.9 Riemannian Submanifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 187
5.10 Totally Geodesic Submanifolds .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191
5.11 Jacobi Fields and Conjugate Points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
5.12 Product of Riemannian Manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197

5.13 Holonomy .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
5.14 Commutator and Curvature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 200
5.15 Solutions of Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
6 Lie Groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
6.1 Lie Groups and Algebras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
6.2 Adjoint Representation and the Killing Form . . . . . . . . . . . . . . . . . . . . . . . . 218
6.3 Connections and Metrics on Lie Groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220
6.4 Maurer–Cartan Equations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
6.5 Invariant Integration on a Compact Lie Group .. . . . . . . . . . . . . . . . . . . . . . 225
6.6 Lie Derivative .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228
6.7 Infinitesimal Isometries. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
6.8 Homogeneous Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235
6.9 Symmetric Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 239
6.10 Solutions of Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
7 Comparison Theorems, Curvature and Topology, and Laplacian. . . . . . 245
7.1 The Simplest Comparison Theorems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
7.2 The Cartan–Hadamard Theorem .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
7.3 Manifolds of Positive Curvature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 249
7.4 Manifolds of Constant Curvature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251
7.5 Laplace Operator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
7.6 Solutions of Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255
8 Appendix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257
8.1 Differentiation of Determinants .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257
8.2 Jacobi Identity for the Commutator of Vector Fields . . . . . . . . . . . . . . . . 258
8.3 The Differential of a 1-Form . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 259
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 265

pp13

Chapter 1
Curves in the Plane

The simplest object of differential geometry is a curve in the plane. The definition of a curve varies between different areas of mathematics. In many cases, it is natural to represent a curve as the trajectory of a moving point. In doing so, one should distinguish between a parameterized curve γ (t) = (x(t), y(t)) and a nonparameterized curve, which is the image of a parameterized curve, i.e., a set in the plane. The functions x(t) and y(t) are not arbitrary. They are usually assumed to be smooth. But even under this assumption, a nonparameterized curve may have corners. This can be avoided by requiring the derivatives x'(t) and y'(t) not to vanish simultaneously. In that case, the parameterized curve is said to be smooth. A smooth nonparameterized curve is the image of a smooth parameterized curve.

Geometry deals with both closed and nonclosed (that is, joining two different points) parameterized curves. A smooth (not necessarily closed) parameterized curve in the plane is a map $γ : [a, b] → \mathbb{R}^2$ such that γ(t) =(x(t), y(t)) , where x and y are smooth functions, and $v(t) = \frac{dγ}{dt} (t) \neq 0$ for all t ∈ [a, b] (we assume that the derivative have finite limits at t = a and t = b). A smooth parameterized curve
$γ : [a, b] → \mathbb{R}^2$ is said to be closed if γ (a) = γ (b) and v(a) = v(b).

The length of a curve $γ : [a, b] → \mathbb{R}^2$ can be defined as the limit of the lengths of polygonal chains with vertices on the curve. In more detail, we choose a partition
$a = t_0 < t_1 < · · · < t_n = b$ of the interval [a, b], consider the polygonal chain $P_0P_1 . . .P_n$, where $P_i = (x(t_i ), y(t_i))$, and find the limit of the lengths of these
polygonal chains as the maximum of the numbers  $\Delta t_i = t_i − t_{i−1}$ tends to zero.

It is easy to show that the length of a curve $γ : [a, b] → \mathbb{R}^2$ is equal to

$$
\int_a^b \sqrt{(x'(t))^2 + (y'(t))^2} dt
$$
 
 Indeed, the length of a polygonal chain $P_0P_1 . . .P_n$ equals
n

$$
\sum_{i=1}^n \sqrt{(x_i − x_{i−1})^2 + (y_i − y_{i−1})^2}
$$

where $x_i = x(t_i)$ and $y_i = y(t_i)$. Using the mean value theorem, we can rewrite this sum in the form $\sum^n_{i=1} \Delta t_i \sqrt{(x'(ξ_i))^2 + (y(η_i))^2}$, where the $ξ_i$ and $η_i$ are some
numbers between $t_{i−1}$ and $t_i}. The limit of this sum has the required form.

The area of the figure bounded by a closed curve $γ : [a, b] → \mathbb{R}^2$ without selfintersections can be defined as the least upper bound for the areas of polygons contained in it and the greatest lower bound for the areas of polygons containing it. A figure for which these two numbers are equal is said to be squarable. The area of nonsquarable figures is not defined.
Any figure bounded by a smooth closed curve is squarable.

The oriented area of a figure bounded by a parameterized closed curve without self-intersections equals the area of this figure in absolute value. When the curve is traversed counterclockwise, the oriented area is positive, and when it is traversed clockwise, the oriented area is negative.

A formula for the oriented area of a figure bounded by a parameterized (possibly self-intersecting) curve can be obtained from the following formula for the oriented area A of the triangle with vertices (0, 0), $(x_1, y_1)$, and $(x_2, y_2)$:

$$
A = \frac{1}{2}(x_1y_2 − x_2y_1).
$$

By analogy with this formula, the oriented area of a polygon with consecutive vertices $(x_i, y_i)$, i = 0, 1, . . . ,n, can be defined as

$$
\frac{1}{2} \sum^n_{i=0}(x_iy_{i+1} − x_{i+1}y_i),
$$

where $(x_{n+1}, y_{n+1}) = (x_0, y_0)$. The polygon may have self-intersections.

The formula for the oriented area of a figure bounded by a closed curve
γ : [a, b] → R2 can now be obtained by choosing a partition a = t0 < t1 <
· · · < tn = b of the interval [a, b], considering a polygon P0P1 . . .Pn, where
Pi = (x(ti), y(ti )), and passing to the limit of the oriented areas of such polygons
as the maximum of the numbers  ti = ti − ti−1 tends to zero.
We set xi = x(ti) and yi = y(ti) and use the mean value theorem: xi+1 =
xi +x
 
(ηi) ti , yi+1 = yi +y
 
(ξi) ti . As a result, we obtain the following formula
for the oriented area of a polygon P0P1 . . .Pn:
1
2
n−1
 
i=0
(x(ti)y
 
(ξi ) − y(ti)x
 
(ηi)) ti ,

where  ti = ti+1 − ti and ξi, ηi ∈ [ti, ti+1]. If the numbers  ti are positive and the
maximum among them tends to zero, then we obtain the integral expression
1
2
  b
a
(xy
  − yx
 
)dt
for the oriented area of the figure bounded by the curve γ . Integrating by parts, it is
easy to showthat
−  b
a
yx
 
dt =   b
a
xy
 
dt.
Indeed,
  b
a
yx
 
dt +   b
a
xy
 
dt = (xy)|b
a
= 0,
because the curve is closed.
Thus, the oriented area A of a figure bounded by a smooth closed curve can be
calculated by any of the following three equivalent formulas:
A = −  b
a
yx
 
dt =   b
a
xy
 
dt = 1
2
  b
a
(xy
  − yx
 
)dt . (1.1)
Problem 1.1 A closed curve γ bounds a convex figure. The endpoints of a chord
of length a + b move on the curve γ . A point M of this chord divides it in the ratio
a : b. As the chord moves, M traces a closed curve γ
 . Prove that the area of the
figure bounded by the curves γ and γ
  equals πab.
1.1 Curvature and the Frenet–Serret Formulas
Let γ (t) =  x(t), y(t)  be a smooth curve. It is often convenient to replace the
parameter t by the arc length parameter s = s(t) =   t
0
 v(τ )  dτ, where v(τ ) =
dγ (τ)
dτ . The arc length parameter is the length of the arc of γ enclosed between the
points γ (0) and γ (t).
For the arc length parameter, we have ds
dt
=  v(t) . Therefore, dγ
ds
= dγ
dt
· dt
ds
=
v(t)
 v(t) , whence

'''

print(t5)

