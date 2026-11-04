"""Comprueba los ejemplos de la clase en Cl(3,0), sin dependencias externas.

Cada índice 0..7 es una máscara de generadores de una hoja de base ordenada:
1, e1, e2, e12, e3, e13, e23, e123.
"""
from math import cos, sin, cosh, sinh, atanh, pi, isclose, sqrt, log


def blade_product(a, b):
    sign = 1
    for i in range(3):
        if a & (1 << i):
            for j in range(i):
                if b & (1 << j):
                    sign = -sign
    return a ^ b, sign


def mv(**coefficients):
    result = [0.0] * 8
    for key, value in coefficients.items():
        result[int(key[1:])] = value
    return result


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def scale(k, a):
    return [k * x for x in a]


def gp(a, b):
    result = [0.0] * 8
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            blade, sign = blade_product(i, j)
            result[blade] += sign * x * y
    return result


def conjugate(a):
    return [x * (-1 if i.bit_count() in (1, 2) else 1)
            for i, x in enumerate(a)]


def reverse(a):
    return [x * (-1 if i.bit_count() in (2, 3) else 1)
            for i, x in enumerate(a)]


def check(a, b, name):
    if not all(isclose(x, y, abs_tol=1e-10, rel_tol=1e-10)
               for x, y in zip(a, b)):
        raise AssertionError(f'{name}: {a} != {b}')
    print(f'OK: {name}')


one, e1, e2, e3, I = (mv(**{f'b{i}': 1}) for i in (0, 1, 2, 4, 7))
e12, e23, e31 = gp(e1, e2), gp(e2, e3), gp(e3, e1)

check(gp(I, I), scale(-1, one), 'I² = -1')
check(gp(I, e1), e23, 'I e1 = e23')
check(gp(scale(-1, e23), scale(-1, e31)), scale(-1, e12),
      'correspondencia cuaterniónica i j = k')

a, b = add(e1, scale(2, e2)), add(scale(3, e1), e2)
check(gp(a, b), add(scale(5, one), scale(-5, e12)),
      'producto de los vectores del ejemplo')
check(gp(gp(a, b), scale(0.1, b)), a, 'recuperación por inversa derecha')
check(gp(add(one, e1), add(one, scale(-1, e1))), mv(), 'divisores de cero')

Rz = add(scale(cos(pi / 4), one), scale(-sin(pi / 4), e12))
Rx = add(scale(cos(pi / 4), one), scale(-sin(pi / 4), e23))
rotate = lambda R, v: gp(gp(R, v), reverse(R))
check(rotate(Rz, e1), e2, 'rotor: e1 gira a e2')
check(rotate(Rz, e2), scale(-1, e1), 'rotor: e2 gira a -e1')
check(rotate(Rz, e3), e3, 'rotor: eje fijo')
check(rotate(gp(Rx, Rz), e1), e3, 'composición: primero z, después x')
check(rotate(gp(Rz, Rx), e1), e2, 'composición: primero x, después z')

# Generadores de Spin(3) y signo de la ecuación cinemática espacial.
G1, G2, G3 = (scale(-0.5, gp(I, e)) for e in (e1, e2, e3))
commutator = lambda A, B: add(gp(A, B), scale(-1, gp(B, A)))
for A, B, C in [(G1, G2, G3), (G2, G3, G1), (G3, G1, G2)]:
    check(commutator(A, B), C, 'conmutador de generadores de so(3)')
omega_bivector = gp(I, e3)
check(scale(0.5, commutator(e1, omega_bivector)), e2,
      'cinemática: v punto = omega cruz v')

phi = atanh(0.6)
L = add(scale(cosh(phi / 2), one), scale(sinh(phi / 2), e1))
boosted = gp(gp(L, one), L)
check(boosted, add(scale(1.25, one), scale(0.75, e1)), 'boost beta = 0.6')
check(gp(boosted, conjugate(boosted)), one, 'intervalo del boost')

# Comprobar la fórmula central del denominador con un multivector mixto.
alpha, beta = 2**2 - 3**2 - (1**2 + 2**2 + 3**2) + (4**2 + 5**2 + 6**2), 2*(2*3-(1*4+2*5+3*6))
v, w = mv(b1=1, b2=2, b4=3), mv(b1=4, b2=5, b4=6)
M = add(add(scale(2, one), v), add(gp(I, w), scale(3, I)))
D = add(scale(alpha, one), scale(beta, I))
check(gp(M, conjugate(M)), D, 'denominador central de la inversa general')
Dinv = scale(1 / (alpha**2 + beta**2), add(scale(alpha, one), scale(-beta, I)))
Minv = gp(conjugate(M), Dinv)
check(gp(M, Minv), one, 'inversa multivectorial por la derecha')
check(gp(Minv, M), one, 'inversa multivectorial por la izquierda')

force, position = scale(10, e2), scale(0.2, e1)
wedge = scale(0.5, add(gp(force, position), scale(-1, gp(position, force))))
check(wedge, scale(-2, e12), 'fuerza exterior posición y signo del momento')

# Parte trivectorial del producto recíproco: dos líneas alabeadas.
f1, r1, f2, r2 = e1, mv(), e2, e3
wedge2 = scale(0.5, add(gp(f2, r2), scale(-1, gp(r2, f2))))
F1, F2 = f1, add(f2, wedge2)
trivector = mv(b7=gp(F1, F2)[7])
check(trivector, I, 'producto recíproco no nulo para líneas alabeadas')


def cross(u, v):
    return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0])


def subtract(u, v):
    return tuple(x-y for x, y in zip(u, v))


point, force_xyz, displacement = (2, -1, 3), (1, 4, -2), (-1, 2, 1)
tau = cross(point, force_xyz)
tau_prime = cross(subtract(point, displacement), force_xyz)
assert tau_prime == subtract(tau, cross(displacement, force_xyz))
print('OK: transformación del momento al cambiar el origen')

# Dos líneas de acción pueden producir una fuerza-momento no reducible a
# una fuerza única: resultante (1,1,0), momento (-1,0,0), producto escalar -1.
f_resultant = (1, 1, 0)
tau_resultant = cross((0, 0, 1), (0, 1, 0))
assert sum(f*t for f, t in zip(f_resultant, tau_resultant)) == -1
print('OK: una fuerza-momento general no satisface la restricción de Plücker')

# Correspondencia entre la rotación vectorial del plano y la compleja,
# ecuaciones (13)-(14): el cambio de signo procede de e12 e1 = -e1 e12.
angle = 0.4
planar_v = add(e1, scale(2, e2))
z = add(one, scale(2, e12))
left_action = gp(add(scale(cos(angle), one), scale(-sin(angle), e12)), planar_v)
complex_action = gp(e1, gp(add(scale(cos(angle), one), scale(sin(angle), e12)), z))
check(left_action, complex_action, 'equivalencia entre rotación de Cl2 y complejos')


def exp_series(A):
    term = one
    result = one
    for k in range(1, 50):
        term = scale(1/k, gp(term, A))
        result = add(result, term)
    return result


v_function = add(scale(0.7, e1), scale(0.2, e2))
radius = sqrt(0.7**2 + 0.2**2)
direction = scale(1/radius, v_function)
check(exp_series(v_function), add(scale(cosh(radius), one), scale(sinh(radius), direction)),
      'exponencial de un vector mediante serie de potencias')
sin_term = v_function
sin_result = v_function
for k in range(1, 25):
    sin_term = scale(-1/((2*k)*(2*k+1)), gp(sin_term, gp(v_function, v_function)))
    sin_result = add(sin_result, sin_term)
check(sin_result, scale(sin(radius), direction), 'seno de un vector euclídeo')
check(exp_series(scale(log(2), v_function)),
      add(scale(cosh(radius*log(2)), one), scale(sinh(radius*log(2)), direction)),
      'potencia dos elevado a un vector')

print('Todos los ejemplos algebraicos comprobados.')
