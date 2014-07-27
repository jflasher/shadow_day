'use strict';

var shadowApp = angular.module('shadowApp', []);

/*
The main controller for the functionality
*/
shadowApp.controller('MainCtrl', ['$scope', '$http', function ($scope, $http) {
  // Start by showing the search and hiding the results
  $scope.showSearch = true;
  $scope.showResults = false;

  // Handle industry search
  $scope.searchIndustry = function () {
    var input = $('#industry-input').val();
    performSearch();
  };

  // Perform the search
  var performSearch = function () {
    var url = 'http://ec2-54-225-111-214.compute-1.amazonaws.com/search';
    $http.get(url).
      success(function (data, status) {
        console.log(data);
        $scope.mentors = data;
        $scope.showSearch = false;
        $scope.showResults = true;        
      }).
      error(function (data, status) {
        console.log('error');
    });
  };
}]);

/*
This directive allows us to pass a function in on an enter key to do what we want.
*/
shadowApp.directive('ngEnter', function () {
    return function (scope, element, attrs) {
        element.bind('keydown keypress', function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    scope.$eval(attrs.ngEnter);
                });
 
                event.preventDefault();
            }
        });
    };
});