# SRA Reads Downloader
Python Script to download reads from NCBI database using only Project ID
The project contains two python scripts download_SRA.py and sra_to_fastq.py

## Requirements
- Python 3 with Biopython library
- prefetch and fastq-dump tool from SRA toolkit to be present in bashrc file

## Instructions to use download_SRA.py
python download_SRA.py --sample sample_id --outdir /path/to/output/directory/

## Instructions to use sra_to_fastq.py
python sra_to_fastq.py --folder /path/to/output/directory/

### Additional
User can also delete .sra files using following command:<br />
find /path/to/output/directory/ -name "\*.sra" -type -delete
