import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-9,0))
w1=cq.Workplane('YZ',origin=(54,0,0))
r=w0.sketch().push([(-76,67.5)]).rect(12,45).push([(-78,76)]).rect(2,2,mode='s').finalize().extrude(32).union(w0.sketch().segment((61,5),(67,3)).segment((82,44)).segment((77,46)).arc((73,24),(61,5)).assemble().finalize().extrude(109)).union(w1.sketch().arc((-97,-53),(-82,-52),(-92,-63)).arc((-15,-51),(-73,2)).segment((-73,-13)).segment((-92,-13)).arc((-99,-32),(-97,-53)).assemble().finalize().extrude(-144))