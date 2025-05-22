import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,9,0))
r=w0.sketch().arc((-50,-5),(-96,-52),(-31,-37)).segment((-20,-37)).segment((-21,-9)).segment((-50,-9)).close().assemble().push([(-65,-36)]).circle(11,mode='s').finalize().extrude(-88).union(w0.sketch().arc((0,51),(-57,0),(8,-38)).arc((100,13),(0,51)).assemble().push([(-10.5,4.5)]).rect(37,27,mode='s').finalize().extrude(69))