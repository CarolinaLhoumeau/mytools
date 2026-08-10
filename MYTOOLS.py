PI_INT=1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
E_INT=7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274
#print(len(str(PI_INT)))

def pi_real(N):
    piii=str(PI_INT)
    N=int(N)
    if N<=0 or N>100:
        raise ValueError("N should be between 0 and 100.")
    saida=str(3.)
    for i in range(N):
        saida+=piii[i]
    return saida

def e_real(N):
    eee=str(E_INT)
    N=int(N)
    if N<=0 or N>100:
        raise ValueError("N should be between 0 and 100.")
    saida=str(2.)
    for i in range(N):
        saida+=eee[i]
    return saida

