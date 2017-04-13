library("data.table")

flights <- fread("Desktop/BIOL3380/Pset7/flights14.csv")

DT=data.table(ID=c("b","b","b","a","a","c"), a=1:6, b=7:12, c=13:18)
DT
class(DT$ID)

#DT[i,j,by]

ans<-flights[origin == "JFK" & month==6L]
head(ans) #print just the first 10 of what is selected

ans<-flights[1:2] #get first two columns
ans

ans<-flights[order(origin, -dest)] #sort ascending origin and descending destination
head(ans)

ans <- flights[, arr_delay] #select[i,j] but i is every row so leave blank select[ ,j]
ans

ans <- flights[, list(arr_delay)] #select specific column
head(ans)

ans <- flights[, .(arr_delay, dep_delay)] #select 2 columns
head(ans)

ans<- flights[, .(delay_arr=arr_delay, delay_dep=dep_delay)] #select and rename two columns
head(ans)

ans <- flights[ ,sum((arr_delay+dep_delay)<0)]
ans #total trips with <0 delay



