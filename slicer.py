#email_slicer
# accept user's email address; split into username, domain and extension

def slice_email():
    print("Welcome to the email slicer!")

    email = input("Enter email: ")
    (username, domain) =  email.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username,
          "\nDomain: ", domain,
          "\nExtension: ", extension)

slice_email()