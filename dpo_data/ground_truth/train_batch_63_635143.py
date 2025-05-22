import cadquery as cq
w0=cq.Workplane('YZ',origin=(-5,0,0))
r=w0.sketch().segment((-100,-39),(8,-39)).segment((6,-40)).segment((23,-47)).segment((23,-78)).segment((83,-78)).segment((83,-12)).segment((100,38)).segment((83,43)).segment((83,75)).segment((41,75)).segment((41,78)).segment((-100,78)).close().assemble().push([(-70,-38.5)]).rect(4,1,mode='s').finalize().extrude(10)