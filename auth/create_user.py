from auth.auth_service import AuthService

def main():
    email = input("Email: ")
    password = input("Senha: ")

    service = AuthService()
    service.create_user(email, password)

if __name__ == "__main__":
    main()
