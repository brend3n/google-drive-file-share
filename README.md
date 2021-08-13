### google-drive-file-share

  

#### API for creating, removing, sharing and adding files to folders in google drive.


#### Use this website links below to follow along to initialize your drive:

	1. https://developers.google.com/drive/api/v3/quickstart/python
	2. https://developers.google.com/workspace/guides/create-project
	3. https://developers.google.com/workspace/guides/create-credentials

#### Supports the following:
	1. Create folder
	2. Remove folder
	3. Add to folder
	4. Share folder

#### Example of use:

`drive = DriveShare()
email = "myemail@gmail.com"
folder_id = drive.create_folder(email=email)
folder_id = drive.insert_to_folder("File.pdf", folderid,"pdf")
`

