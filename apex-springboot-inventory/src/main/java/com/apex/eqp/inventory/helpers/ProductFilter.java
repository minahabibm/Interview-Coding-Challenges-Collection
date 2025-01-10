package com.apex.eqp.inventory.helpers;

import com.apex.eqp.inventory.entities.Product;
import com.apex.eqp.inventory.entities.RecalledProduct;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

public class ProductFilter {

    private static List<RecalledProduct> recalledProducts;

    public ProductFilter(List<RecalledProduct> recalledProducts) {
        if (recalledProducts == null) recalledProducts = new ArrayList<>();

        this.recalledProducts = recalledProducts;
    }

    public List<Product> removeRecalled(Collection<Product> allProduct) {
        return allProduct.stream().filter(ProductFilter::filterByName).collect(Collectors.toList());
    }

    private static boolean filterByName(Product product) {
        for(int i=0; i < recalledProducts.size(); i++)
            if(recalledProducts.get(i).getName().equals(product.getName())) return false;
        return true;
    }
}
