import socket
import re
import gmpy2
import binascii

# --- CONFIGURATION ---
HOST = 'verbal-sleep.picoctf.net'
PORT = 64886
E_VALUE = 65537 # The known public exponent from the server code
MAX_ATTEMPTS = 200 # Try collecting 200 different N, C pairs

# --- CORE MATH FUNCTIONS ---

def solve_rsa(N, e, C):
    """
    Factors N, calculates d, and decrypts the ciphertext C.
    """
    # 1. Collect all N values for GCD checks
    N_list = []
    
    # Check GCD between all collected N values to find a shared prime factor 'p'
    # This is an optimization: we only need to factor N, then we can decrypt.
    # We will assume a prime factor 'p' is found from N_list.
    
    # For simplicity, we will assume N is already factored into p and q 
    # (since the GCD attack is the only way to proceed without knowing the server's 'setup.py').
    
    print("\n--- Starting GCD Attack to find a shared factor p ---")
    
    # 1. Collect N, C pairs
    N_list = []
    C_map = {} # Map N to C for quick lookup later
    
    i = 0
    while i < MAX_ATTEMPTS:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            data = s.recv(4096).decode('utf-8')
            s.close()

            # Parse N and C values
            n_match = re.search(r'N:\s*(\d+)', data)
            c_match = re.search(r'cyphertext:\s*(\d+)', data)
            
            if n_match and c_match:
                N_val = int(n_match.group(1))
                C_val = int(c_match.group(1))
                
                if N_val not in N_list:
                    N_list.append(N_val)
                    C_map[N_val] = C_val
                    print(f"Collected pair {i+1}/{MAX_ATTEMPTS}: N={N_val}... C={C_val}...")
                    
                    # 2. Check for shared factors among all collected N values
                    if len(N_list) > 1:
                        for N_prev in N_list[:-1]:
                            p = gmpy2.gcd(N_val, N_prev)
                            
                            if p > 1: # Found a shared factor!
                                print("\n!!! SHARED FACTOR FOUND !!!")
                                print(f"p = gcd(N_current, N_prev) = {p}")
                                
                                # We can now factor both N_val and N_prev
                                q_val = N_val // p
                                q_prev = N_prev // p
                                
                                # Use the factors for the current N, C pair
                                N_target = N_val
                                C_target = C_val
                                break # Exit inner loop
                        else: # If inner loop completed without break
                            i += 1
                            continue # Continue outer loop

                        break # Exit outer loop if shared factor found
                    
                    i += 1
            else:
                 print("Error: Could not parse N and C from server response. Check server output format.")
                 print(f"Received data:\n{data}")
                 return

        except ConnectionRefusedError:
            print(f"Connection failed. Ensure the server is running at {HOST}:{PORT}")
            return
        except Exception as e:
            print(f"An error occurred during collection/GCD: {e}")
            return
            
    # --- Decryption Phase ---
    if p > 1:
        # 3. Calculate Euler's Totient function: phi(N) = (p-1)(q-1)
        phi_N = (p - 1) * (q_val - 1)
        
        # 4. Calculate private key 'd': d = inverse(e, phi(N))
        d = gmpy2.invert(E_VALUE, phi_N)
        
        # 5. Decrypt the ciphertext: M = C^d mod N
        M_int = pow(C_target, d, N_target)
        
        # 6. Output the Message
        M_hex = hex(M_int)[2:]
        if len(M_hex) % 2 != 0:
            M_hex = '0' + M_hex
        M_bytes = binascii.unhexlify(M_hex)

        print("\n=============================================")
        print("🔓 DECRYPTION SUCCESS: Message (M) Found via GCD Attack")
        print(f"Prime p: {p}")
        print(f"Prime q: {q_val}")
        print(f"Private Key d: {d}")
        print(f"Message (ASCII/Flag): {M_bytes.decode('utf-8', errors='ignore')}")
        print("=============================================")
    else:
        print("\n--- Attack Failed ---")
        print("Could not find a shared factor after all attempts. The 'get_primes' function may be secure.")


if __name__ == "__main__":
    solve_rsa(None, E_VALUE, None)
