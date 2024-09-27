immutable_var = (1, 2, [1, 2, 3, 4])
print(immutable_var)
  #immutable_var[1] = 10          в кортеже не удастся изменить объекты
mutable_list = immutable_var
mutable_list[2][1] = 10
print(mutable_list)



