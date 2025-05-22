import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,25,0))
w1=cq.Workplane('YZ',origin=(-61,0,0))
r=w0.sketch().push([(-43,51)]).circle(26).circle(7,mode='s').finalize().extrude(-79).union(w0.sketch().push([(-1,-65.5)]).rect(40,23).push([(70.5,6)]).rect(59,18).finalize().extrude(-15)).union(w0.workplane(offset=-10/2).moveTo(-1,-65.5).box(30,21,10)).union(w1.sketch().arc((-7,-4),(10,-100),(10,-3)).segment((10,12)).segment((22,12)).segment((22,-1)).segment((32,-1)).segment((32,34)).segment((-7,34)).close().assemble().finalize().extrude(82))