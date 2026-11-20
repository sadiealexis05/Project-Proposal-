# Revisiting Higher-Order Masked Comparison for Lattice-Based Cryptography: Algorithms and Bit-sliced Implementations 

Group Members: Teagan Hawkins, Jackie Medrano, Sadie Salcido

Overview:
Revisiting Higher-Order Masked Comparison for Lattice-Based Cryptography: Algorithms and Bit-sliced Implementations is a paper in which researchers set out to optimize the masked comparison step within the Fujisaki-Okamoto (FO). Rather than designing entirely new cryptographic algorithms, they introduced new mathematical techniques and software optimizations such as bit-slicing implementations to make this comparison faster at higher masking orders. They evaluated these optimizations by implementing and benchmarking them using existing lattice-based schemes, Kyber and Saber, on an ARM Cortex-M4 microcontroller.

Scholarly paper references:
-  [1]J.-P. D’Anvers, M. Van Beirendonck, and I. Verbauwhede, “Revisiting Higher-Order Masked Comparison for Lattice-Based Cryptography: Algorithms and Bit-Sliced Implementations,” Cryptology ePrint Archive, 2022. https://eprint.iacr.org/2022/110 (accessed Oct. 2026).

-  [2]J.-S. Coron, F. Gérard, S. Montoya, and R. Zeitoun, “High-Order Polynomial Comparison and Masking Lattice-Based Encryption,” IACR Transactions on Cryptographic Hardware and Embedded Systems, pp. 153–192, Nov. 2022, doi: 10.46586/tches.v2023.i1.153-192.

Recreating environment(cloning,building,deploying):

