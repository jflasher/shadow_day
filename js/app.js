'use strict';

// API root url
// var apiRoot = 'http://ec2-54-225-111-214.compute-1.amazonaws.com/';
var apiRoot = 'http://127.0.0.1:8000/';

var shadowApp = angular.module('shadowApp', []);

/*
The main controller for the functionality
*/
shadowApp.controller('MainCtrl', ['$scope', '$http', function ($scope, $http) {

  ////
  // Initial values
  ////
  // Start by showing the search and hiding the results
  $scope.showSearch = true;
  $scope.showResults = false;
  $scope.heading = 'Find a shadow for a day';

  // Get possible values for degree and industry searches
  $http.get(apiRoot + 'industries').
    success(function (data, status) {
      $scope.safeApply(function () {
        $scope.industries = data;
      });
    }).
    error(function (data, status) {
      console.log('error');
  });

  $http.get(apiRoot + 'degrees').
    success(function (data, status) {
      $scope.degrees = data;
    }).
    error(function (data, status) {
      console.log('error');
  });

  ////
  // End initial value setting
  ////

  // Handle industry search
  $scope.searchIndustry = function () {
    var selectedIndex = $('#industry-input').val();
    var input = $scope.industries[selectedIndex].name;
    console.log(input);
    var heading = 'Find a shadow for a day in the ' + input + ' industry.';
    performSearch(input, 'industry', heading);
  };

  $scope.searchDegree = function () {
    var selectedIndex = $('#degree-input').val();
    var input = $scope.degrees[selectedIndex].name;
    console.log(input);
    var heading = 'Find a shadow for a day with a degree in ' + input;
    performSearch(input, 'degree', heading);
  };  

  // Perform the search
  var performSearch = function (input, endpoint, heading) {
    var url = apiRoot + 'search?' + endpoint + '=' + input;
    console.log(url);
    $http.get(url).
      success(function (data, status) {
        console.log(data);
        $scope.mentors = data;
        $scope.heading = heading;
        $scope.showSearch = false;
        $scope.showResults = true;        
      }).
      error(function (data, status) {
        console.log('error');
    });
  };

  // Go back from search results
  $scope.goBack = function () {
    $scope.showResults = false;
    $scope.showSearch = true;
  };

  $scope.safeApply = function(fn) {
    var phase = this.$root.$$phase;
    if(phase === '$apply' || phase === '$digest') {
      if(fn && (typeof(fn) === 'function')) {
        fn();
      }
    } else {
      this.$apply(fn);
    }
  };    
}]);