import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,25,0))
w1=cq.Workplane('YZ',origin=(21,0,0))
r=w0.sketch().push([(-43,52)]).circle(25).circle(6,mode='s').finalize().extrude(-79).union(w0.sketch().segment((-23,-77),(14,-77)).segment((14,-66)).segment((41,-66)).segment((41,-65)).segment((14,-65)).segment((14,-3)).segment((-23,-3)).close().assemble().push([(67,6)]).rect(66,18).finalize().extrude(-15)).union(w1.sketch().arc((-7,-5),(1,-100),(20,-6)).segment((32,-6)).segment((32,34)).segment((-7,34)).close().assemble().push([(14,5)]).circle(10,mode='s').finalize().extrude(-82))