data<-read.csv("~/code/stats/project/500-url-title-wikipedia-wiki-stock.csv")

nonzero_edit_volume_data<-subset(data, data$EditVolume>0)



plot(nonzero_edit_volume_data$EditVolume ~ nonzero_edit_volume_data$StockVolume, main="Stock Volume and Edit Volume", xlab="Stock Volume", yaxt="n", ylab="Edit Volume", xaxt="n")
axis(side=2, at=seq(0, max(data$EditVolume), length.out = 4), labels=humanReadable(seq(0, max(data$EditVolume), length.out = 4), standard="SI"))
axis(side=1, at=seq(0, max(data$StockVolume), length.out = 4), labels=as.integer(seq(0, max(data$StockVolume), length.out = 4)))

plot(log(nonzero_edit_volume_data$EditVolume) ~ log(nonzero_edit_volume_data$StockVolume), main="Stock Volume and Edit Volume", sub="After logarithmic transformation", xlab="Stock Volume", ylab="Edit Volume", yaxt="n", xaxt="n")
y_labels<-seq(log(1), log(max(nonzero_edit_volume_data$EditVolume)), length.out = 10)
axis(side=2, at=y_labels, labels=humanReadable(exp(y_labels)))
x_labels<-seq(log(1), log(max(nonzero_edit_volume_data$StockVolume)), length.out = 11)
axis(side=1, at=x_labels, labels=FALSE)
text(x_labels, par("usr")[3] - 0.55, labels=as.integer(exp(x_labels)), srt=40, pos=1, xpd=TRUE)

log_r<-cor(log(nonzero_edit_volume_data$EditVolume), log(nonzero_edit_volume_data$StockVolume))
log_r
model<-lm(log(nonzero_edit_volume_data$EditVolume) ~ log(nonzero_edit_volume_data$StockVolume))
model
abline(model)

edit_count_hist<-hist(data$EditCount, breaks="FD", plot=FALSE, xaxt='n')
plot(edit_count_hist, main="Edits Per Company", xlab="Page's monthly edit count", ylab="Number of pages", col=heat.colors(length(edit_count_hist$counts)))
edit_count_sd<-sd(data$EditCount)
edit_count_mean<-mean(data$EditCount)

edit_count_volume<-hist(data$EditVolume, breaks=c(0,exp(seq(log(1), log(max(data$EditVolume)), length.out=15))), plot=FALSE)
plot(edit_count_volume, main="Edit Volume Per Company", xlab="Page's monthly edit volume", freq=T, ylab="Number of pages", col=heat.colors(length(edit_count_volume$counts)), xaxt='n')
axis(side=1, at=seq(0, max(data$EditVolume), length.out = length(edit_count_volume$breaks)), labels=humanReadable(edit_count_volume$breaks, standard="SI"))
edit_volume_sd<-sd(data$EditVolume)
edit_volume_mean<-mean(data$EditVolume)

scd_hist<-hist(data$StockChangeDirection, plot=T, breaks="FD", xlab="Percent change in stock price", ylab="Number of companies", main="Percent Change in Stock Price Per Company", col=heat.colors(length(scd_hist$counts)))
boxplot(data$StockChangeDirection, main="Percent change in stock price", ylab="Percent change in stock price")

scd_sd<-sd(data$StockChangeDirection)
scd_mean<-mean(data$StockChangeDirection)

scv_hist<-hist(data$StockVolume, plot=T, breaks="FD", xlab="Trading volume", ylab="Number of companies", main="Trading Volume Per Company", col=heat.colors(length(scv_hist$counts)))
scv_sd<-sd(data$StockVolume)
scv_mean<-mean(data$StockVolume)

cor(data$EditCount, data$StockVolume)
cor(data$EditCount, data$StockChangeMagnitude)
cor(data$EditCount, data$StockChangeDirection)

cor(data$EditVolume, data$StockVolume)
cor(data$EditVolume, data$StockChangeMagnitude)
cor(data$EditVolume, data$StockChangeDirection)

cor(data$EditCount, data$EditVolume)
cor(data$StockVolume, data$StockChangeMagnitude)
cor(data$StockVolume, data$StockChangeDirection)

# Filter the data appropriately
nonzero_edit_data<-subset(data, data$EditCount>0)
all_edit_data<-data

# Collect sample statistics
nonzero_edit_data_n<-length(nonzero_edit_data$EditCount)
nonzero_edit_data_mean_volume<-mean(nonzero_edit_data$StockVolume)

# Collect population parameters
all_edit_data_mean_volume<-mean(all_edit_data$StockVolume)
all_edit_data_sd_volume<-sd(all_edit_data$StockVolume)

# Compute z and effect size
nonzero_edit_data_z<-(nonzero_edit_data_mean_volume-all_edit_data_mean_volume)/(all_edit_data_sd_volume/sqrt(nonzero_edit_data_n))
nonzero_edit_data_d<-(nonzero_edit_data_mean_volume-all_edit_data_mean_volume)/(all_edit_data_sd_volume)

# Filter the data appropriately
nonzero_change_data<-subset(data, data$StockChangeMagnitude>=0.01)
all_change_data<-data

# Collect sample statistics
nonzero_change_data_n<-length(nonzero_change_data$Ticker)
nonzero_change_data_mean_edit_count<-mean(nonzero_change_data$EditCount)

# Collect population parameters
all_change_data_mean_edit_count<-mean(all_change_data$EditCount)
all_change_data_sd_edit_count<-sd(all_change_data$EditCount)

# Calculate z and effect size
nonzero_change_data_z<-(nonzero_change_data_mean_edit_count-all_change_data_mean_edit_count)/(all_change_data_sd_edit_count/sqrt(nonzero_change_data_n))
nonzero_change_data_d<-(nonzero_change_data_mean_edit_count-all_change_data_mean_edit_count)/(all_change_data_sd_edit_count)
