import cadquery as cq
w0=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().arc((-57,-15),(-38,-67),(11,-91)).segment((11,-100)).segment((22,-100)).segment((22,-91)).arc((90,-22),(30,55)).arc((-67,87),(-57,-15)).assemble().finalize().extrude(51)