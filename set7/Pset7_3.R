v1 %*% v2
m=matrix(
  c(1,2,3,4,5,6),
  nrow = 3,
  ncol = 2
)
m
#t(m) transposes the matrix into a 2x3
v = c(3,1)
m %*% v #should give a 3x1 matrix if it auto transposes
v %*% m #should give an error because it transposes the vector and not the matrix
