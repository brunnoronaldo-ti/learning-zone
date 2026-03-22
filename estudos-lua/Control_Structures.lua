-- Control Structures in Lua
-- Note that we use "then" and "end".

local fruits = {"apple", "Banana", "orange"}
local xp = 100

-- if-elseif-else structure
if xp >= 100 then
    print("Level Up!")
elseif xp >= 50 then
    print("Halfway there!")
else
    print("Keep going!")
end

-- loops

for i = 1, 5 do
    print("Contagem: " .. i)
end

for index, valor in ipairs(fruits) do
    print(index, valor)
end

-- While loop
local count = 1

while count <= 5 do
    print("Contagem: " .. count)
    count = count + 1
end

