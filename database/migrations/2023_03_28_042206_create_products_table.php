<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('products', function (Blueprint $table) {
            $table->id();
            $table->string('title');
            $table->string('slug');
            $table->integer('user_id');
            $table->integer('category_id');
            $table->integer('subcategory_id');
            $table->integer('brand_id');
            $table->integer('barcode');
            $table->boolean('status');
            $table->string('short_description');
            $table->longtext('long_description');
            $table->float('price');
            $table->string('price_currency');
            $table->string('add_price_method');
            $table->float('add_price');
            $table->string('add_price_currency');
            $table->string('tax_method');
            $table->float('tax_price');
            $table->string('tax_currency');
            $table->string('weight_type');
            $table->float('weight_amount');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('products');
    }
};
