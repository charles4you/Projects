import imaplib

def Connect_to_Outlook (Email, Password):

    # use your email provider's IMAP server, for office 365, it's this:
    imap_server = "outlook.office365.com"

    # create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL(imap_server)

    # authenticate
    imap.login(Email, Password)

    return imap


def Search_in_Outlook(Email_from, Subject, imap):

    # Select the Inbox folder
    status, messages = imap.select("INBOX")

    # Search the emails from Banorte
    result, data = imap.search(None, '(SINCE "01-Jan-2023" FROM "'+Email_from+'" SUBJECT "'+Subject+'")')

    # Make the list of data, a separate item for each email
    ids = data[0]
    id_list = ids.split()
    return id_list, data

