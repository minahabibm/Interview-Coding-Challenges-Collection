from itertools import combinations
import time

def openFileToList(fileName):
  f = open(fileName, "r")
  data=[]
  for coordinates in f:
    coordinatesData = [float(item) for item in coordinates.replace("(", "").replace(")", "").rstrip().split(",")]
    data.append(coordinatesData)
  f.close() 
  return data

def volume_of_tetrahedron(p1, p2, p3, p4):
  # Vectors from p1 to p2, p3, and p4
  AB = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
  AC = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
  AD = (p4[0] - p1[0], p4[1] - p1[1], p4[2] - p1[2])

  # Direct calculation of the cross product components
  cross_product_x = AB[1] * AC[2] - AB[2] * AC[1]
  cross_product_y = AB[2] * AC[0] - AB[0] * AC[2]
  cross_product_z = AB[0] * AC[1] - AB[1] * AC[0]

  # Dot product of AD with the cross product of AB and AC
  scalar_triple_product = (
    AD[0] * cross_product_x +
    AD[1] * cross_product_y +
    AD[2] * cross_product_z
  )

  # The volume of the tetrahedron
  volume = abs(scalar_triple_product) / 6.0
  return volume

def findMinPoint(coordinates, coordinates_points):
  lowest_point = None
  lowest_vol = float('inf')
  for coordinate in coordinates_points:
    vol = volume_of_tetrahedron(coordinates[coordinate[0]][:3], coordinates[coordinate[1]][:3], coordinates[coordinate[2]][:3], coordinates[coordinate[3]][:3])
    if(vol < lowest_vol):
      lowest_point = (coordinate)
      lowest_vol = vol
  print("Smallest possible volume:", lowest_vol)
  print("Indices of valid tetrahedron:", lowest_point)


def fourSumCombinations(coordinates):
  combinations_of_points = combinations(enumerate(coordinates), 4)
  valid_combinations = []
  for combo in combinations_of_points:
    combo_indices, combo_points = zip(*combo)
    if sum(point[3] for point in combo_points) == 100:
      valid_combinations.append(combo_indices)
  return valid_combinations

def fourSumBF(coordinates):
  res = set()
  for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
      for k in range(j + 1, len(coordinates)):
        for l in range(k + 1, len(coordinates)):
          sum_of_fourth_values = coordinates[i][3] + coordinates[j][3] + coordinates[k][3] + coordinates[l][3]
          if sum_of_fourth_values == 100:
            res.add((i,j,k,l))
  return res

def fourSum(coordinates):
  n = len(coordinates)
  target = 100
  #ans = []
  # unique_set = set()

  lowest_point = None
  lowest_vol = float('inf')
    
  indexed_coords = [(coord, idx) for idx, coord in enumerate(coordinates)]
  indexed_coords.sort(key=lambda x: x[0][3])

  for i in range(n-3):
    for j in range(i + 1, n-2):
      hashmap = {}
      for k in range(j+1, n):
        complement = target - (indexed_coords[i][0][3] + indexed_coords[j][0][3] + indexed_coords[k][0][3])
        if complement in hashmap:
          for pair in hashmap[complement]:
            coordinate = (indexed_coords[i][1], indexed_coords[j][1], pair, indexed_coords[k][1])
            # unique_set.add(tuple(sorted(coordinate)))
            
            vol = volume_of_tetrahedron(coordinates[indexed_coords[i][1]][:3], coordinates[indexed_coords[j][1]][:3], coordinates[pair][:3], coordinates[indexed_coords[k][1]][:3])
            if(vol < lowest_vol):
              lowest_point = (tuple(sorted(coordinate)))
              lowest_vol = vol
  
        if indexed_coords[k][0][3] in hashmap:
          hashmap[indexed_coords[k][0][3]].add(indexed_coords[k][1])
        else:
          hashmap[indexed_coords[k][0][3]] = {indexed_coords[k][1]}

  # print("Number of valid tetrahedrons:", len(ans))
  print("Smallest possible volume:", lowest_vol)
  print("Indices of the Smallest valid tetrahedron:", lowest_point)
  # ans = list(unique_set)
  # return ans


def findValidTetrahedron(fileName):
  coordinates = openFileToList(fileName)

  # start_time = time.time()
  #fourSumCombinations((points[0],points[1],points[2],points[3]) for points in coordinates)
  # end_time = time.time()
  # print(end_time - start_time)

  # start_time = time.time()
  # coordinates_points = fourSumBF(coordinates)
  # end_time = time.time()
  # print(end_time - start_time)

  # findMinPoint(coordinates, coordinates_points)

  start_time = time.time()
  fourSum(coordinates)
  end_time = time.time()
  print(f"Completed in {end_time - start_time} seconds")

def main():
  print("points_small.txt valid tetrahedrons:")
  findValidTetrahedron("points_small.txt")
  print()
  print("points_large.txt valid tetrahedrons:")
  findValidTetrahedron("points_large.txt")


if __name__ == "__main__":
  main()