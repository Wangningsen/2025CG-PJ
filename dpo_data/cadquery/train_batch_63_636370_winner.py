import cadquery as cq
w0=cq.Workplane('YZ',origin=(-44,0,0))
w1=cq.Workplane('XY',origin=(0,0,-25))
r=w0.sketch().circle(83).circle(55,mode='s').finalize().extrude(141).union(w0.sketch().arc((12,53),(-54,-48),(54,11)).segment((54,-29)).segment((24,-29)).segment((24,18)).segment((53,18)).arc((38,38),(17,51)).arc((15,51),(12,53)).assemble().finalize().extrude(144)).union(w1.sketch().push([(-33,-2)]).circle(67).push([(-12,29)]).circle(19,mode='s').finalize().extrude(-15))