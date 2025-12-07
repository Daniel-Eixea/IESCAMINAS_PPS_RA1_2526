// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleMerkle {
    // Guarda la raíz del Merkle Tree
    bytes32 public merkleRoot;

    // Constructor inicializa la raíz (puedes usar cualquier hash de ejemplo)
    constructor() {
        // Hash de ejemplo (SHA256 de "dato1")
        merkleRoot = 0x3a6eb0781e9eb0e27c8a8eb1e4f9a8ee2a7f712f35f1df6ff12b0ff7f16c9b7b;
    }

    // Función para actualizar la raíz (opcional)
    function updateRoot(bytes32 _newRoot) public {
        merkleRoot = _newRoot;
    }
}