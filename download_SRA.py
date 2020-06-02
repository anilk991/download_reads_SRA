from Bio import Entrez
import lxml.etree
import os
import argparse as ap

def get_ids(project):
	han = Entrez.esearch(db='sra', term=project, retmax=2000)
	rec = Entrez.read(han)
	results = record['IdList']
	return results

def get_accession(ids):
	accessions = []
	for _id in ids:
		handle = Entrez.efetch(db='sra', id=_id, retmode="text")
		en = lxml.etree.parse(handle)
		acc_ = en.xpath('//EXPERIMENT_PACKAGE_SET/EXPERIMENT_PACKAGE/RUN_SET/RUN/@accession')[0]
		accessions.append(acc_)
	return accessions

def download(accs, outdir):
	for acc in accs:
		os.system('prefetch -p -O ' + outdir + ' ' + acc)

if __name__ == '__main__':
	parser = ap.ArgumentParser()
	parser.add_argument('--sample', type=str, help='Sample ID')
	parser.add_argument('--outdir', type=str, help='Output Directory')
	args = parser.parse_args()
	
	ids = get_ids(args.sample)
	accs = get_accession(ids)
	download(accs, args.outdir)