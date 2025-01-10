package com.apex.eqp.inventory;

import com.apex.eqp.inventory.entities.Product;
import com.apex.eqp.inventory.entities.RecalledProduct;
import com.apex.eqp.inventory.services.ProductService;
import com.apex.eqp.inventory.services.RecalledProductService;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

@SpringBootTest
class ProductServiceTests {

    @Autowired
    ProductService productService;

    @Autowired
    RecalledProductService recalledProductService;

    /**
     * Helper method to create test products
     */
    private Product createTestProduct(String productName, Double price, Integer quantity) {
        return Product.builder()
                .name(productName)
                .price(price)
                .quantity(quantity)
                .build();
    }

    /**
     * Helper method to create test recalled products
     */
    private RecalledProduct createTestRecalledProduct(String recalledProductName) {
        return RecalledProduct.builder()
                .name(recalledProductName)
                .build();
    }

    @Test
    void shouldSaveProduct() {
        Product product = createTestProduct("product1", 1.2, 2);

        Product savedProduct = productService.save(product);

        Product loadedProduct = productService.findById(savedProduct.getId()).orElse(null);

        Assertions.assertNotNull(loadedProduct);
        Assertions.assertNotNull(loadedProduct.getId());
    }

    @Test
    void shouldUpdateProduct() {
        Product product = createTestProduct("product2", 1.3, 5);

        Product savedProduct = productService.save(product);

        Product loadedProduct = productService.findById(savedProduct.getId()).orElse(null);

        Assertions.assertNotNull(loadedProduct);

        loadedProduct.setName("NewProduct");

        productService.save(loadedProduct);

        Assertions.assertNotNull(productService.findById(loadedProduct.getId()).orElse(null));
    }

    @Test
    void shouldSaveRecalledProducts() {
        RecalledProduct recalledProduct = createTestRecalledProduct("recalledProduct");

        RecalledProduct savedRecalledProduct = recalledProductService.save(recalledProduct);

        Collection recalledProducts = recalledProductService.getAllRecalledProducts();

        Assertions.assertNotNull(recalledProducts);

    }

    @Test
    void shouldGetAllProductsList() {
        Product product = createTestProduct("product", 1.3, 5);
        Product recProduct = createTestProduct("RecProduct", 1.3, 5);
        RecalledProduct recalledProduct = createTestRecalledProduct("RecProduct");

        Product savedProduct = productService.save(product);
        Product savedProducts = productService.save(recProduct);
        RecalledProduct savedRecalledProduct = recalledProductService.save(recalledProduct);

        Collection allProduct = productService.getAllProduct();

        Assertions.assertNotNull(allProduct);

    }


}
