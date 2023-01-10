Genre = str(input("Enter The Genre:"))

Anime = {'Adventure':'one Piece,Naruto, Hunter X Hunter, Samuraichamploo,Claymore','Action':'My Hero Academia,Bleach,Dragon Ball,Attack on Titan,OnePunch Man','Horror':'Angels of Death,Happy sugar life,Berserk,Another','Fantasy':'The seven deadly sins!, Sword art online, Fairy tail, Re:Zero Starting life in Another world , No game No life ,Log horizon , How not to summon a demon lord,Made in Abyss , Akame ga kill, is it wrong to pick girls in dungeon?'}
if Genre == 'Adventure':
   print(Anime['Adventure'])
elif Genre =='Action':
   print(Anime['Action'])
elif Genre =='Horror':
   print(Anime['Horror'])
elif Genre =='Fantasy':
   print(Anime['Fantasy'])