def tower_of_hanoi(n, source, target, auxiliary):
  if n == 1:
    print(f"Move disk 1 from {source} to {target}")
    return 1
   
  moves = 0
   
  moves += tower_of_hanoi(n-1, source, auxiliary, target)
   
  print(f"Move disk {n} from {source} to {target}")
  moves += 1
   
  moves += tower_of_hanoi(n-1, auxiliary, target, source)
   
  return moves

   
n = int(input("Enter number of disks: "))

print("\nSolution:\n")
total_moves = tower_of_hanoi(n, 'A', 'C', 'B')

print("\nTotal moves =", total_moves)
