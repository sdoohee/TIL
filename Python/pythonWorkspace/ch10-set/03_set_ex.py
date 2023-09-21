partyA = {"Park", "Kim", "Lee"}
partyB = {"Park", "길동", "몽룡"}

print("파티에 참석한 모든 사람")
print(partyA | partyB)
print("---------------------------------------")
print("2개의 파티에 모두 참석한 사람")
print(partyA & partyB)
print("---------------------------------------")
print("파티A에만 참석한 사람")
print(partyA - partyB)
print("---------------------------------------")
print("파티B에 참석한 사람")
print(partyB - partyA)
print("---------------------------------------")



######################################################
print("파티에 참석한 모든 사람")
print(partyA | partyB)
print(partyA.union(partyB))
print("------------------------")

print("2개의 파티에 모두 참석한 사람")
print(partyA & partyB)
print(partyA.intersection(partyB))
print("------------------------")

print("파티A에만 참석한 사람")
print(partyA - partyB)
print(partyA.difference(partyB))
print("------------------------")

print("파티B에만 참석한 사람")
print(partyB - partyA)
print(partyB.difference(partyA))
print("------------------------")