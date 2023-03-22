[Byte[]] $key = (1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 11, 12, 13, 14, 15, 16)
# generates file password.txt in current directory, pasword encrypted with key
$File = "Password.txt"

# in %%%%%%% is where the password is supposed to go
$Password = "%%%%%%%%" | ConvertTo-SecureString -AsPlainText -Force
$Password | ConvertFrom-SecureString -key $key | Out-File $File
