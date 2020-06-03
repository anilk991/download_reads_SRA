from glob import glob
import argparse as ap
import os
import sys
import time

parser = ap.ArgumentParser()
parser.add_argument('--folder', type=str, help='Folder where SRA files were downloaded')
args = parser.parse_args()

start = time.time()

path = args.folder
if not path.endswith('/'):
	path += '/'

# Creating list of all files ending with .sra and an additional *
# because download_SRA.py stores all files in a new folder
sra = glob(path + '*/*.sra')


# First part of for loop is for checking progress
# Second part saves fastq files in the same folder containing .sra files
for i in range(len(sra)):
	sys.stdout.write('\r')
	sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
	sys.stdout.flush()
	
	split_path = sra[i].split('/')
	split_path = split_path[:-1]
	outpath = '/'.join(split_path) + '/'
	os.system('fastq-dump --split-files --outdir ' + outpath + ' ' + sra[i])
	
end = time.time()

print('\n' + 'Total time taken: ' + str((end - start)/60) + ' minutes.\n')
print(str(len(sra)) + ' sra files were converted to fastq format.\n')
