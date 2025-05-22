import cadquery as cq
w0=cq.Workplane('YZ',origin=(-79,0,0))
r=w0.sketch().segment((-48,41),(-17,-28)).segment((-17,-100)).segment((17,-100)).segment((17,-55)).segment((48,-41)).segment((17,28)).segment((17,100)).segment((-17,100)).segment((-17,55)).close().assemble().circle(19,mode='s').finalize().extrude(158)