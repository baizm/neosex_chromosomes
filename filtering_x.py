import subprocess


api_ind = '/scratch/lsa_flux/baizm/individuals/api_ind_2.txt' #individuals from lanes12 who did not show admixture in fastStructure
apm_ind = '/scratch/lsa_flux/baizm/individuals/apm_ind_2.txt' #individuals from lanes12 who did not show admixture in fastStructure
api_F = '/scratch/lsa_flux/baizm/individuals/api_ind_F.txt'
api_M = '/scratch/lsa_flux/baizm/individuals/api_ind_M.txt'
apm_F = '/scratch/lsa_flux/baizm/individuals/apm_ind_F.txt'
apm_M = '/scratch/lsa_flux/baizm/individuals/apm_ind_M.txt'
in_vcf = '/scratch/lsa_flux/baizm/snpCalling/filtered_final_2.vcf'
out_dir = '/scratch/lsa_flux/baizm/neosex/x_loci/'
vcftools = '/home/baizm/vcftools_0.1.12b/bin/vcftools'

#filter vcf to keep only bi-allelic markers
subprocess.call("bcftools view -m2 -M2 %s > %sbiallelic.vcf" % (in_vcf, out_dir), shell=True)
#filter vcf to keep only sites with minimum mean depth of 10 across individuals
subprocess.call("%s --vcf %sbiallelic.vcf --min-meanDP 10 --recode --out %sbiallelic_DP10" % (vcftools, out_dir, out_dir), shell=True)

#subset vcfs by species
subprocess.call("bcftools view -S %s %sbiallelic_DP10.recode.vcf > %sapi.vcf" % (api_ind, out_dir, out_dir), shell=True)
subprocess.call("bcftools view -S %s %sbiallelic_DP10.recode.vcf > %sapm.vcf" % (apm_ind, out_dir, out_dir), shell=True)

#make vcfs with sites present in at least 50% of individuals in each parental pop
subprocess.call("%s --vcf %sapm.vcf --max-missing 0.50 --recode --out %sapm_50" % (vcftools, out_dir, out_dir), shell=True)
subprocess.call("%s --vcf %sapi.vcf --max-missing 0.50 --recode --out %sapi_50" % (vcftools, out_dir, out_dir), shell=True)

#subset vcfs by sex
subprocess.call("bcftools view -S %s %sapi_50.recode.vcf > %sapi_F.vcf" % (api_F, out_dir, out_dir), shell=True)
subprocess.call("bcftools view -S %s %sapi_50.recode.vcf > %sapi_M.vcf" % (api_M, out_dir, out_dir), shell=True)
subprocess.call("bcftools view -S %s %sapm_50.recode.vcf > %sapm_F.vcf" % (apm_F, out_dir, out_dir), shell=True)
subprocess.call("bcftools view -S %s %sapm_50.recode.vcf > %sapm_M.vcf" % (apm_M, out_dir, out_dir), shell=True)
