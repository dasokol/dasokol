var heatmapInstance = h337.create({
	container: document.getElementById('heatmap'), 
	radius: 28,
	maxOpacity: .75,
	blur: 1,
	gradient: {
	    // enter n keys between 0 and 1 here
	    // for gradient color customization
	    '.4': 'blue',
	    '.4': 'green',
	    '.75': 'yellow',
	    '.7': 'orange',
	    '1': 'red'
	}
});
 
document.getElementById('heatmap').onmousemove = function(ev) {
	heatmapInstance.addData({
    	x: ev.layerX,
        y: ev.layerY,
        value: 1
    });
};
