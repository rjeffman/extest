# SPDX-License-Identifer: MIT

#
# This is an example code. There should be none on this directory.
#

"""Implementação do exercício zero."""


def procura_maior(lista):
    """Procura maior item na lista usando procura linear."""
    maior = lista[0]
    for item in lista[1:]:
        if item > maior:
            maior = item
    return maior


def procura_menor(lista):
    """Procura menor item na lista."""
    return min(lista)

