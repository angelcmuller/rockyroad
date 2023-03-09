const express = require("express");
const recordRoutes = express.Router();
const dbo = require("../db/conn");

recordRoutes.route("/record").get(function(req, res) {
  let db_connect = dbo.getDb("pinDatabase");
  db_connect.collection("Pins").find({}).toArray(function(err, result) {
    if (err) throw err;
    let output = JSON.stringify(result);
    console.log(output);
    res.send(output);
  });
});

recordRoutes.route("/crecord").get(function(req, res) {
  let db_connect = dbo.getDb("pinDatabase");
  db_connect.collection("Comments").find({}).toArray(function(err, result) {
    if (err) throw err;
    let output = JSON.stringify(result);
    console.log(output);
    res.send(output);
  });
});

recordRoutes.route("/conrecord").get(function(req, res) {
  let db_connect = dbo.getDb("pinDatabase");
  db_connect.collection("Cpins").find({}).toArray(function(err, result) {
    if (err) throw err;
    let output = JSON.stringify(result);
    console.log(output);
    res.send(output);
  });
});

module.exports = recordRoutes;
