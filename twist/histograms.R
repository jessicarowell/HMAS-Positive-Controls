library(ggplot2)
library(RColorBrewer)


nf <- read.table("gc_found.txt", header = F)
f <- read.table("gc_not_found.txt", header = F)

nf$group <- "not found"
f$group <- "found"

a <- rbind(f, nf)

png("histogram.png")

ggplot(a, aes(x=GC, fill=Group, color=Group)) + geom_histogram(binwidth=3, position="identity", alpha=0.5)
 + theme(axis.text=element_text(size = 18)) + scale_color_manual(values=c("#1B9E77","#E7298A")) + scale_fill_manual(values=c("#1B9E77","#E7298A"))

dev.off()

