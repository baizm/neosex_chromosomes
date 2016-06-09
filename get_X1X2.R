setwd('~/Documents/Dissertation/Neo-sex Chromosome/x_loci/')

#APA
m<-read.table('depth_apm_M.ldepth.mean', header=T)
f<-read.table('depth_apm_F.ldepth.mean', header=T)
ratios<-data.frame(contig=m[,1], pos=m[,2], FtoM=f$MEAN_DEPTH/m$MEAN_DEPTH)
hist(log2(ratios$FtoM), xlab='Log2(F:M depth)', xlim=c(-0.5,2), ylim=c(0,20000), breaks=200, main='Apa F:M depth')
x<-subset(ratios, subset=log2(ratios$FtoM)>0.5)
x_loci<-data.frame(loci=paste(x$contig, x$pos))

#API
m2<-read.table('depth_api_M.ldepth.mean', header=T)
f2<-read.table('depth_api_F.ldepth.mean', header=T)
ratios2<-data.frame(contig=m2[,1], pos=m2[,2], FtoM=f2$MEAN_DEPTH/m2$MEAN_DEPTH)
hist(log2(ratios2$FtoM), xlab='Log2(F:M depth)', xlim=c(-1,1.5), ylim=c(0,50000), breaks=200, main='Api F:M depth')
x2<-subset(ratios2, subset=log2(ratios2$FtoM)>0.5)
x2_loci<-data.frame(loci=paste(x2$contig, x2$pos))

#find shared log2(F:M)>0.5 sites
shared<-merge(x_loci,x2_loci) #7176 loci!
write.table(shared, file='candidateX1X2_shared.txt', quote=F, row.names=F, col.names=F)

#then use get_SNP_seqs.py & cat candidateX1X2_shared300bp.txt | xargs -n 1 samtools faidx ../../reference_genome/AloPal_combined.a.lines.fasta > candidateX1X2_shared300bp.fasta 
#to extract candidate X1X2 sequences from reference
