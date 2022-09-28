#!/bin/bash

flask db upgrade

flask seed all
