import pytest
import subprocess

def test_single_DNS():
    d = subprocess.check_output("mpirun -np 1 python TG.py NS", shell=True)

def test_single_dealias_DNS():
    d = subprocess.check_output("mpirun -np 1 python TG.py --dealias '3/2-rule' NS", shell=True)

def test_single_DNS2():
    d = subprocess.check_output("mpirun -np 1 python TG.py --optimization cython NS", shell=True)

def test_single_DNS3():
    d = subprocess.check_output("mpirun -np 1 python TG.py --M 6 6 6 NS", shell=True)
    
def test_single_DNS4():
    d = subprocess.check_output("mpirun -np 1 python TG.py --M 6 5 4 --L 6*pi 4*pi 2*pi NS", shell=True)

def test_single_DNS5():
    d = subprocess.check_output("mpirun -np 1 python TG.py --M 4 4 4 --write_result 5 NS", shell=True)
    
def test_single_DNS2D():
    d = subprocess.check_output("mpirun -np 1 python TG2D.py NS2D", shell=True)
    
def test_single_VV():
    d = subprocess.check_output("mpirun -np 1 python TG.py VV", shell=True)

def test_single_VV2():
    d = subprocess.check_output("mpirun -np 1 python TG.py --optimization cython VV", shell=True)

def test_single_KMM():
    d = subprocess.check_output("mpirun -np 1 python OrrSommerfeld.py --optimization cython KMM", shell=True)

def test_single_IPCS():
    d = subprocess.check_output("mpirun -np 1 python OrrSommerfeld.py --optimization cython IPCS", shell=True)

def test_mpi_slab_DNS():
    d = subprocess.check_output("mpirun -np 4 python TG.py NS", shell=True)

def test_mpi_slab_DNS():
    d = subprocess.check_output("mpirun -np 4 python TG.py --write_result 5 NS", shell=True)

def test_mpi_DNS2D():
    d = subprocess.check_output("mpirun -np 4 python TG2D.py NS2D", shell=True)

def test_mpi_dealias_DNS():
    d = subprocess.check_output("mpirun -np 4 python TG.py --dealias '3/2-rule' NS", shell=True)

def test_mpi_pencil_DNS():
    d = subprocess.check_output("mpirun -np 4 python TG.py --decomposition pencil --P1 2 --write_result 5 NS", shell=True)

#def test_mpi_pencil_dealias_DNS():
    #d = subprocess.check_output("mpirun -np 4 python TG.py --decomposition pencil --P1 2 --dealias '3/2-rule' NS", shell=True)

def test_mpi_pencil_DNS2():
    d = subprocess.check_output("mpirun -np 8 python TG.py --decomposition pencil --P1 2 --write_result 5 NS", shell=True)
    
def test_mpi_slab_VV():
    d = subprocess.check_output("mpirun -np 4 python TG.py VV", shell=True)

def test_mpi_pencil_VV():
    d = subprocess.check_output("mpirun -np 4 python TG.py --decomposition pencil --P1 2 VV", shell=True)
    
def test_single_MHD():
    d = subprocess.check_output("mpirun -np 1 python TGMHD.py --write_result 5 MHD", shell=True)
    
def test_mpi_slab_MHD():
    d = subprocess.check_output("mpirun -np 4 python TGMHD.py --write_result 5 MHD", shell=True)
    
def test_mpi_pencil_MHD():
    d = subprocess.check_output("mpirun -np 4 python TGMHD.py --decomposition pencil --P1 2 --write_result 5 MHD", shell=True)
    
#def test_mpi_slab_DNS2D():
#    d = subprocess.check_output("mpirun -np 4 python TG2D.py NS2D", shell=True)

def test_mpi_KMM():
    d = subprocess.check_output("mpirun -np 4 python OrrSommerfeld.py --optimization cython --write_result 5 --checkpoint 5 KMM", shell=True)

def test_mpi_IPCS():
    d = subprocess.check_output("mpirun -np 4 python OrrSommerfeld.py --optimization cython --write_result 5 --checkpoint 5 IPCS", shell=True)