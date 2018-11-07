import os
def generateImportStatement(fileName, schemaName, tableName):
    """ 
    caution windows users will have to use ROW SEPARATOR = 'CRLF'
    """    
    return f"""IMPORT INTO {schemaName}.{tableName}
FROM LOCAL CSV FILE '{fileName}'
ENCODING = 'UTF-8'
ROW SEPARATOR = 'LF'
COLUMN SEPARATOR = ','
COLUMN DELIMITER = '"'
SKIP = 1
REJECT LIMIT 0;

"""

def writeCsvstoSQLCmds(csvlocation, schemaName, tableName):
	"""
	file extension can also be changed to .sql if wanted to make it executable
	it is txt so you can copy it to the db client of your choice and execute it
	"""
	sqlfile = open("sqlcommands.txt","w")
	csvfiles = os.listdir(csvlocation);
	for csvfile in csvfiles:
		sqlfile.write(generateImportStatement(csvfile,schemaName,tableName))
