"""
********************************************************************************
numerical
********************************************************************************

.. currentmodule:: compas.numerical


Solvers
=======

.. autosummary::
    :toctree: generated/
    :nosignatures:

    devo_numpy
    dr
    dr_numpy
    fd_numpy
    ga
    moga
    pca_numpy
    topop_numpy


Linalg
======

.. autosummary::
    :toctree: generated/
    :nosignatures:

    nullspace
    rank
    dof
    pivots
    nonpivots
    rref
    rref_sympy
    rref_matlab
    chofactor
    lufactorized
    uvw_lengths
    normrow
    normalizerow
    rot90
    solve_with_known
    spsolve_with_known


Matrices
========

.. autosummary::
    :toctree: generated/
    :nosignatures:

    adjacency_matrix
    degree_matrix
    connectivity_matrix
    laplacian_matrix
    face_matrix
    mass_matrix
    equilibrium_matrix


Operators
=========

.. autosummary::
    :toctree: generated/
    :nosignatures:

    grad


Utilities
=========

.. autosummary::
    :toctree: generated/
    :nosignatures:

    float_formatter
    set_array_print_precision
    unset_array_print_precision


"""
from __future__ import absolute_import

import compas

if not compas.IPY:
    from .linalg import (
        nullspace,
        rank,
        dof,
        pivots,
        nonpivots,
        rref,
        rref_sympy,
        rref_matlab,
        uvw_lengths,
        normrow,
        normalizerow,
        rot90,
        solve_with_known,
        spsolve_with_known,
        chofactor,
        lufactorized
    )
    from .matrices import (
        adjacency_matrix,
        degree_matrix,
        connectivity_matrix,
        laplacian_matrix,
        face_matrix,
        mass_matrix,
        stiffness_matrix,
        equilibrium_matrix,
    )
    from .operators import (
        grad,
        div,
        curl
    )
    from .utilities import (
        float_formatter,
        set_array_print_precision,
        unset_array_print_precision
    )

if not compas.IPY:
    from .descent import descent_numpy
    from .topop import topop_numpy
    from .pca import pca_numpy
    from .ga import ga, moga
    from .fd import fd_numpy
    from .dr import dr_numpy
    from .devo import devo_numpy
    from .isolines import scalarfield_contours_numpy


__all__ = []

if not compas.IPY:
    __all__ += [
        'nullspace',
        'rank',
        'dof',
        'pivots',
        'nonpivots',
        'rref',
        'rref_sympy',
        'rref_matlab',
        'uvw_lengths',
        'normrow',
        'normalizerow',
        'rot90',
        'solve_with_known',
        'spsolve_with_known',
        'chofactor',
        'lufactorized',
        'adjacency_matrix',
        'degree_matrix',
        'connectivity_matrix',
        'laplacian_matrix',
        'face_matrix',
        'mass_matrix',
        'stiffness_matrix',
        'equilibrium_matrix',
        'grad',
        'div',
        'curl',
        'float_formatter',
        'set_array_print_precision',
        'unset_array_print_precision',
    ]
    __all__ += [
        'descent_numpy',
        'topop_numpy',
        'pca_numpy',
        'ga',
        'moga',
        'devo_numpy',
        'fd_numpy',
        'dr_numpy',
        'scalarfield_contours_numpy'
    ]
