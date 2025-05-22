import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
w1=cq.Workplane('ZX',origin=(0,-17,0))
r=w0.sketch().segment((1,8),(15,8)).arc((33,-6),(50,8)).segment((60,8)).segment((60,13)).segment((50,9)).arc((34,30),(15,12)).segment((5,36)).segment((60,58)).segment((60,100)).segment((1,100)).close().assemble().finalize().extrude(-39).union(w1.sketch().segment((-11,-60),(80,-60)).segment((80,23)).segment((12,23)).arc((-19,26),(-11,-5)).close().assemble().reset().face(w1.sketch().arc((6,-3),(60,-39),(14,6)).arc((11,1),(6,-3)).assemble(),mode='s').finalize().extrude(-83))