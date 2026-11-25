# Lecture 5 - Mini lesson plan

## Configuration files

1. Why ? Easy design, human readibility without code interference, cross platform compatibility ; you have less code
2. How ? The CSV/TSV format, constant files in python / javascript
3. What ? Anything that is constant across the experiment : Stimuli and their properties, conditions, gui... sometimes it is interesting to have multiple configuration files!

## Configuration files in javascript

### Demo

Papaparse library : a js file to include to the project

```{js}
export function parseCSVFile(url) {
  return new Promise((resolve, reject) => {
    Papa.parse(url, {
      download: true,
      header: true,
      skipEmptyLines: true,
      transform: value => value.trim(),
      complete: resolve,
      error: reject,
    });
  });
}
```

What is a promise ? asynchrony in js

### Setting up a local server

when you start loading files, you will no longer be able to open your files using absolute path in your browser (you will have a cross reference error)

To solve that, you will need a local server
`python -m http.server`

Note that this only work on linux and mac, windows provide less intuitive ways of setting up a server that I can't test!

### Exercise s

Add a configuration file to your stroop task :
- Colors and response keys should be configured
