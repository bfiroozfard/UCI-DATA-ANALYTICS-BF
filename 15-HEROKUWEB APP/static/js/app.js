function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
  // Use d3 to select the panel with id of `#sample-metadata`
    var url1=`/metadata/${sample}`;
    console.log(url1);
     
    // Use `.html("") to clear any existing metadata
     

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    d3.json(url1).then(function(response) {
    console.log(response); 
    d3.select("#sample-metadata").html("");
    Object.entries(response).forEach(([key,value])=>{
    d3.select('#sample-metadata').append('p').text(`${key}:${value}`).append('hr');
    })
    })
}

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots

  var url=`/samples/${sample}`;
  console.log(url);
  d3.json(url).then(function(response) {

    console.log(response);
  // @TODO: Build a Bubble Chart using the sample data
    var trace1 = {
  x: response.otu_ids,
  y: response.sample_values,
  mode: 'markers',
  marker: {
    color: response.otu_ids,
    
    size: response.sample_values
  }
};

var data = [trace1];

var layout = {
  title: 'Belly Button Bubble Chart',
  showlegend: false
  //height: 600,
  //width: 600
}


Plotly.newPlot('bubble', data, layout);

// @TODO: Build a Pie Chart
// HINT: You will need to use slice() to grab the top 10 sample_values,
// otu_ids, and labels (10 each).

var data1 = [{
  values: response.sample_values.slice(0,10),
  labels: response.otu_ids.slice(0,10),
   // hovertext =response.otu_labels.slice(0,10),
  type: 'pie'
}];

var layout1 = {
  title: '<b> Belly Button Pie Chart </b>'
  //height: 400,
  //width: 500
};

Plotly.newPlot('pie', data1, layout1);

  });
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();