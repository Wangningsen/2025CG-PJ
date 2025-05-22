import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
w1=cq.Workplane('ZX',origin=(0,-47,0))
r=w0.sketch().push([(74,-78)]).circle(22).circle(6,mode='s').finalize().extrude(-59).union(w0.sketch().push([(-76,80)]).circle(20).push([(-93,78)]).circle(2,mode='s').finalize().extrude(91)).union(w1.sketch().arc((12,-16),(17,-20),(20,-25)).arc((23,-26),(27,-28)).segment((88,-28)).segment((88,5)).segment((27,5)).segment((27,2)).arc((18,-3),(12,-11)).arc((13,-14),(12,-16)).assemble().finalize().extrude(7))