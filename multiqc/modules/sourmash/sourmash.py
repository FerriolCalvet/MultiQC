#!/usr/bin/env python

""" MultiQC module to parse output from sourmash """

import logging

from multiqc.modules.base_module import BaseMultiqcModule

from .compare import CompareMixin

# Initialise the logger
log = logging.getLogger(__name__)


class MultiqcModule(BaseMultiqcModule, CompareMixin):
    def __init__(self):
        super(MultiqcModule, self).__init__(
            name="Sourmash",
            anchor="sourmash",
            href="https://github.com/sourmash-bio/sourmash",
            info="quickly searches, compares, and analyzes genomic and metagenomic data sets.",
            doi="10.21105/joss.00027",
        )

        n = dict()
        n["compare"] = self.parse_compare()
        if n["compare"] > 0:
            log.info("Found {} compare results".format(n["compare"]))

        if sum(n.values()) == 0:
            raise UserWarning
