from PyPDF2 import PdfFileWriter, PdfFileReader


def decrypt_pdf(filename, password):
    # Create a PdfFileWriter object
    out = PdfFileWriter()

    # Open encrypted PDF file with the PdfFileReader
    file = PdfFileReader(filename)

    # Check if the opened file is actually Encrypted
    if file.isEncrypted:

        # If encrypted, decrypt it with the password
        file.decrypt(password)

        # Now, the file has been unlocked.
        # Iterate through every page of the file
        # and add it to our new file.
        for idx in range(file.numPages):
            # Get the page at index idx
            page = file.getPage(idx)

            # Add it to the output file
            out.addPage(page)

        # Open a new file "myfile_decrypted.pdf"
        with open(filename, "wb") as f:

            # Write our decrypted PDF to this file
            out.write(f)

        # Print success message when Done
        print("File decrypted Successfully.")
    else:
        # If file is not encrypted, print the
        # message
        print("File already decrypted.")
