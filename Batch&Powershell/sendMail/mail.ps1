[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
# username is the mail
$Username = "%%%"

#password
$secpasswd = "%%%"

# mail info
$EmailTo = "%%%%" 
$EmailFrom = $Username
$Subject = "Test mail"
$Body = "body text"

# the mail from which it is sent is an office mail
$SMTPServer = "smtp.office365.com" 
$port = "587"

$SMTPMessage = New-Object System.Net.Mail.MailMessage
$SMTPMessage.Subject = $Subject
$SMTPMessage.Body = $Body
$SMTPMessage.From = $EmailFrom
$SMTPMessage.To.Add($EmailTo)

$SMTPMessage.IsBodyHTML=$true

$SMTPClient = New-Object Net.Mail.SmtpClient($SmtpServer, $port) 
$SMTPClient.EnableSsl = $true 
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential($Username, $secpasswd); 
$SMTPClient.Send($SMTPMessage)

write-host "Mail Sent"